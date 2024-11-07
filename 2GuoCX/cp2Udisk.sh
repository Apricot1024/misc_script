 #!/bin/bash

prefix="202401Q3D"


# Get the mount point of the portable disk
echo "Please make sure your U disk has been connected correctly!(Press enter to continue)"
read
mount_point=$(df | grep "/media/KINGSTON" | awk '{print $6}')

# Check if the mount point is valid
if [ -z "$mount_point" ]; then
  echo "No portable disk found. Please connect your portable disk and try again."
  exit 1
fi

echo "Get U disk at $mount_point done."

[ ! -d "${mount_point}/${prefix}" ] && mkdir -p "${mount_point}/${prefix}"
# Get the round_numbers from the user
echo "Enter round_numbers (e.g., 1,3-5,7), (0 to exit):"
read round_numbers

# Loop until the user enters the stop flag '0'
while [[ $round_numbers != "0" ]]; do
    IFS=',' read -ra round_numbers_array <<< "$round_numbers"

    # Convert each page number range to a list of individual page numbers.
    for round_number in "${round_numbers_array[@]}"; do
        # Check if the page number is a range.
        if [[ "$round_number" =~ - ]]; then
            round_numbers_array=(${round_numbers_array[@]/$round_number/})
            # Split the page number range into start and end page numbers.
            start_round_number=${round_number%-*}
            end_round_number=${round_number#*-}

            # Create a list of individual page numbers in the range.
            round_numbers_list=$(seq $start_round_number $end_round_number)
        else
            # The page number is not a range, so just add it to the list.
            round_numbers_list=$round_number
        fi

        # Add the list of individual page numbers to the array of page numbers.
        round_numbers_print+=($round_numbers_list)
    done
  
    # Copy the files with the specified round_numbers
    for round_number in "${round_numbers_print[@]}"; do
        cp /wdaq/${prefix}${round_number}.root /media/${mount_point}/
        cp /wdaq/${prefix}${round_number}.log /media/${mount_point}/
        echo "Copy round ${round_number} done."
    done

    unset round_numbers_print
    # Prompt the user to enter new round_numbers or the stop flag '0'
    echo "Enter round_numbers (e.g., 1,3-5,7), (0 to exit):"
    read round_numbers
done

# Unmount the portable U disk
umount /media/${mount_point}
echo "Umount done."

echo "All done."