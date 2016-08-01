//Program to check if all characters in a string are unique

//Take String from user
var str = prompt("Enter a string to check uniqueness: ")
//console.log(str)


function check_char_uniqueness(str) {
    
        //Let's make a JS Object
        var frequency_tracker = { };
        //console.log(frequency_tracker);

        //Loop through each characters in string
        for (var index in str) {
            //console.log(str[index]); //loop through chars not indexes

            //if character alreay exists as key in object frequency_tracker
            //then increment it
            //otherwise just enter it with default value 1

            //frequency_tracker[str[index]] = frequency_tracker[str[index]] +1 || 1;
            //console.log(frequency_tracker);

            //This program can be even shorter
            //return false at the same moment you see that key already exists
            //in this case, if character already exists we don't even need to proceed further

            if ( frequency_tracker[str[index]] in Object.keys(frequency_tracker)) {
                return false;
            } else {
                 frequency_tracker[str[index]] = 1;
            }
        }
    
    //ultimately true is return if no repeatitive char is found
    return true;    
}

//If function return true
//print all characters are unique in string
//If function returns false
//simply print Not Unique

check_char_uniqueness(str) ? console.log("All Characters in provided string are unique!") : console.log("Not Unique!");

//console.log(check_char_uniqueness(str));
