import * as readline from "readline";
import * as fs from "fs";
import * as lodash from "lodash";

// function to convert every string separated by a space into an array

// function to convert the dash string formatted "X-Y" into a range(X-Y)
function stringToRange(str: String) {
    // Split the string into two parts (X and Y) using the split method
    const [x, y] = str.split('-')

    const start = parseInt(x, 10);
    const end = parseInt(y, 10);

    // Use the lodash range function to create a range from X to Y
    return lodash.range(start, end + 1);
}

// Create a new instance of the readline interface
const rl = readline.createInterface({
  input: fs.createReadStream('day4.txt')
});

const strings = rl.split(/\s+/);

// Convert each element in the array of strings into an element in the list
const list = strings.map((str: any) => str.trim());
console.log(list)

rl.on('line', function(line: String) {
    stringToRange(list)
});
