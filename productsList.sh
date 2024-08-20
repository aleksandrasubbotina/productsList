#! /bin/bash

# Create a list of unique product IDs and quantity parameter
# in JSON format
function ids() {
    LIST=""
    for ((i=1;i<=$1;i++))
    do
        NEW="id: $i, "quantity": 1"
        LIST+="{$NEW}, "
    done
    # Remove space and comma at the end of the list
    echo ${LIST%??}
}

# User input: amount of product names needed in the list
read -p "Enter number of product names: " COUNT

# Check if input is integer
re='^[0-9]+$'
if [[ $COUNT =~ $re ]]
then
    # Result string and output
    RESULT=$(ids $COUNT)
    echo "{"productsList":[$RESULT]}"
else
    echo "Error: please enter a number"
fi