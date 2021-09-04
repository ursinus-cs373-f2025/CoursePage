class Adder {
    /**
     * Construct an adder inside of a particular DOM element with four rows:
     * top row is for carry
     * middle two are for adding
     * bottom is for result
     * @param {string} elemId 
     */
    constructor(elemId) {
        const elem = document.getElementById(elemId);
        this.label = document.createElement("p");
        this.label.setAttribute("style", "font-size: x-large;");
        elem.appendChild(this.label);
        this.table = document.createElement("table");
        elem.appendChild(this.table);
        this.N = 0;
        this.stepIdx = 0;
        this.carry = 0;
    }

    /**
     * @param {int} x Base 10 number to add
     * @param {int} y Base 10 number to add
     */
    setupAdder(x, y) {
        this.label.innerHTML = "Click the Step button to show one step of the addition";
        const table = this.table;
        table.innerHTML = ""; // Reset table from last time
        this.x = base10ToBinary(x);
        this.y = base10ToBinary(y);
        const z = base10ToBinary(x+y);
        this.z = x + y;
        this.N = z.length;
        while (this.x.length < this.N) {
            this.x = "0" + this.x;
        }
        while (this.y.length < this.N) {
            this.y = "0" + this.y;
        }
        const carryRow = document.createElement("tr");
        table.appendChild(carryRow);
        this.carryCols = [];
        
        const xRow = document.createElement("tr");
        table.appendChild(xRow);
        this.xCols = [];
        
        const yRow = document.createElement("tr");
        table.appendChild(yRow);
        this.yCols = [];
        
        const lineRow = document.createElement("tr");
        table.appendChild(lineRow);
        const line = document.createElement("td");
        line.setAttribute("style", "height:1px;");
        line.setAttribute("colspan", ""+(this.N+1));
        line.innerHTML = "<HR>";
        lineRow.appendChild(line);

        const addRow = document.createElement("tr");
        table.appendChild(addRow);
        this.addCols = [];

        // Setup columns
        const rows = [carryRow, xRow, yRow, addRow];
        const lists = [this.carryCols, this.xCols, this.yCols, this.addCols];
        // Dummy column for +
        let lefttds = [];
        for (let k = 0; k < lists.length; k++) {
            const td = document.createElement("td");
            rows[k].appendChild(td);
            lefttds[k] = td;
        }
        lefttds[2].innerHTML = "<h3>+</h3>";
        this.stepButton = document.createElement("button");
        this.stepButton.setAttribute("type", "button");
        this.stepButton.innerHTML = "Step";
        this.stepButton.onclick = this.stepAdder.bind(this);
        this.stepButton.setAttribute("style", "width:140px;");
        lefttds[3].appendChild(this.stepButton);
        this.restartButton = document.createElement("button");
        this.restartButton.setAttribute("type", "button");
        this.restartButton.innerHTML = "Restart";
        this.restartButton.onclick = this.restartAdder.bind(this);
        this.restartButton.setAttribute("style", "width:140px;");
        lefttds[3].appendChild(document.createElement("p")); // Spacing
        lefttds[3].appendChild(this.restartButton);
        lefttds[3].setAttribute("style", "width:200px;");
        for (let i = 0; i < this.N; i++) {
            for (let k = 0; k < lists.length; k++) {
                const td = document.createElement("td");
                lists[k][i] = td;
                rows[k].appendChild(td);
            }
        }
        // Put x and y digits into their rows
        for (let i = 0; i < this.N; i++) {
            this.xCols[i].innerHTML = this.x[i];
            this.yCols[i].innerHTML = this.y[i];
        }
        // Add columns at the end for the answer
        let righttds = [];
        for (let k = 0; k < lists.length; k++) {
            const td = document.createElement("td");
            rows[k].appendChild(td);
            righttds[k] = td;
            lists[k][lists[k].length] = td;
        }
        righttds[1].innerHTML = "<h3>= " + x + "<SUB>10</SUB></h3>";
        righttds[2].innerHTML = "<h3>= " + y + "<SUB>10</SUB></h3>";
        this.stepIdx = this.N-1;
        this.carry = 0;
    }

    restartAdder() {
        this.label.innerHTML = "";
        for (let i = 0; i < this.xCols.length; i++) {
            this.xCols[i].setAttribute("style", "");
            this.yCols[i].setAttribute("style", "");
            this.addCols[i].setAttribute("style", "");
            this.addCols[i].innerHTML = "";
            this.carryCols[i].innerHTML = "";
            this.addCols[this.addCols.length-1].innerHTML = "";
        }
        this.stepIdx = this.N-1;
    }


    stepAdder() {
        if (this.stepIdx >= 0) {
            // Undo last stuff
            // Get rid of second to last carry
            if (this.stepIdx < this.N-1) {
                this.carryCols[this.stepIdx+1].innerHTML = "";
            }
            if (this.stepIdx < this.N-1) {
                // Un-bold last positions
                this.xCols[this.stepIdx+1].setAttribute("style", "");
                this.yCols[this.stepIdx+1].setAttribute("style", "");
                this.addCols[this.stepIdx+1].setAttribute("style", "");
            }
            // Do next step
            this.xCols[this.stepIdx].setAttribute("style", "font-weight: bold; color:red;");
            this.yCols[this.stepIdx].setAttribute("style", "font-weight: bold; color:red;");
            let x = parseInt(this.x[this.stepIdx]);
            let y = parseInt(this.y[this.stepIdx]);
            this.label.innerHTML = "";
            if (this.carry > 0) {
                this.label.innerHTML += this.carry + " + ";
            }
            this.label.innerHTML += x + " + " + y;
            let res = this.carry + x + y;
            this.carry = Math.floor(res/2);
            res = res % 2;
            this.label.innerHTML += " = " + res;
            if (this.carry > 0) {
                this.label.innerHTML += ", carry 1";
            }
            if (this.carry > 0) {
                this.carryCols[this.stepIdx-1].innerHTML = this.carry;
                this.carryCols[this.stepIdx-1].setAttribute("style", "font-weight: bold; color:red;")
            }
            this.addCols[this.stepIdx].innerHTML = res;
            this.addCols[this.stepIdx].setAttribute("style", "font-weight: bold; color:red;");
            this.stepIdx -= 1;
        }
        else {
            this.carryCols[1].innerHTML = "";
            if (this.carryCols.length > 1) {
                this.carryCols[2].innerHTML = "";
            }
            this.addCols[1].setAttribute("style", "");
            this.xCols[1].setAttribute("style", "");
            this.yCols[1].setAttribute("style", "");
            this.addCols[this.addCols.length-1].innerHTML = "<h3>= " + this.z + "<SUB>10</SUB></h3>";
            
            this.label.innerHTML = "That's it!";

        }
    }
}

CIRCLE_WIDTH= 50;
class BinaryClock {
    constructor() {
        let canvas = document.getElementById('clockCanvas');
        let ctx = canvas.getContext("2d"); //For drawing
        this.ctx = ctx;
        this.canvas = canvas;
        ctx.font = "16px Arial";
        //Need this to disable that annoying menu that pops up on right click
        canvas.addEventListener("contextmenu", function(e){ e.stopPropagation(); e.preventDefault(); return false; }); 
        this.repaint();
    }

    repaint() {
        const W = this.canvas.width;
        const H = this.canvas.height;
        const ctx = this.ctx;
        ctx.clearRect(0, 0, W, H);
        // Hours
        let date = new Date();
        let b = base10ToBinary(date.getHours());
        while (b.length < 5) {
            b = "0" + b;
        }
        let y = CIRCLE_WIDTH*0.8;
        for (let i = 0; i < 5; i++) {
            ctx.beginPath();
            let x = CIRCLE_WIDTH*(i+2)*1.5;
            ctx.arc(x, y, CIRCLE_WIDTH/2, 0, 2*Math.PI, false);
            if (b[i] == "1") {
                ctx.fillStyle = 'red';
            }
            else {
                ctx.fillStyle = 'black';
            }
            ctx.fill();
            ctx.lineWidth = 5;
            ctx.strokeStyle = '#003300';
            ctx.stroke();
        }

        // Minutes
        b = base10ToBinary(date.getMinutes());
        while (b.length < 6) {
            b = "0" + b;
        }
        y = CIRCLE_WIDTH*2;
        for (let i = 0; i < 6; i++) {
            ctx.beginPath();
            let x = CIRCLE_WIDTH*(i+1)*1.5;
            ctx.arc(x, y, CIRCLE_WIDTH/2, 0, 2*Math.PI, false);
            if (b[i] == "1") {
                ctx.fillStyle = 'red';
            }
            else {
                ctx.fillStyle = 'black';
            }
            ctx.fill();
            ctx.lineWidth = 5;
            ctx.strokeStyle = '#003300';
            ctx.stroke();
        }

        // Seconds
        b = base10ToBinary(date.getSeconds());
        while (b.length < 6) {
            b = "0" + b;
        }
        y = CIRCLE_WIDTH*3.2;
        for (let i = 0; i < 6; i++) {
            ctx.beginPath();
            let x = CIRCLE_WIDTH*(i+1)*1.5;
            ctx.arc(x, y, CIRCLE_WIDTH/2, 0, 2*Math.PI, false);
            if (b[i] == "1") {
                ctx.fillStyle = 'red';
            }
            else {
                ctx.fillStyle = 'black';
            }
            ctx.fill();
            ctx.lineWidth = 5;
            ctx.strokeStyle = '#003300';
            ctx.stroke();
        }
        setTimeout(this.repaint.bind(this), 100);
    }
}


/**
 * 
 * @param {int} x A number in base 10
 * @returns A binary string representing x
 */
function base10ToBinary(x) {
    let rem = x;
    let b = "";
    let place = 2;
    do {
        if (rem%place == 0) {
            b = "0" + b;
        }
        else {
            b = "1" + b;
        }
        rem -= rem%place;
        place *= 2;
    }
    while (rem > 0);
    return b;
}

/**
 * 
 * @param {string} b A binary string
 * @returns An int corresponding to the binary string
 */
function binaryToBase10(b) {
    let s = b.split("").reverse().join("");
    let place = 1;
    let x = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] == "1") {
            x += place;
        }
        place *= 2;
    }
    return x;
}

/**
 * 
 * @param {string} b A binary string
 * @returns The HTML code to create a table showing the number
 *          in binary with its places
 */
function makeBinaryTableStr(b) {
    let s = "";
    s += "<table border = 1 cellpadding=10><tr>";
    let place = Math.pow(2, b.length-1);
    for (let i = 0; i < b.length; i++) {
        s += "<td><h3>" + place + "</h3></td>";
        place /= 2;
    }
    s += "</tr><tr>";
    for (let i = 0; i < b.length; i++) {
        s += "<td><h3>" + b[i] + "</h3></td>";
    }
    s += "</tr></table>";
    return s;
}

/**
 * 
 * @param {string} b A binary string
 * Make the HTML code showing how to convert a binary string to base 10
 */
function makeShowBinarySumStr(b) {
    let s = "<h2>";
    place = Math.pow(2, b.length-1);
    for (let i = 0; i < b.length; i++) {
        s += "<font color=red>" + b[i] + "</font>*<font color=green>" + place+"</font>";
        if (i < b.length - 1) {
            s += "+ ";
        }
        else {
            s += " = ";
        }
        place /= 2;
    }
    s + "</code><BR>"
    s += "<b>" + binaryToBase10(b) + "</b></h2>";
    return s;
}












HEX_VALS = "0123456789ABCDEF";
HEX_VAL_TO_NUM = {};
for (let i = 0; i < 10; i++) {
    HEX_VAL_TO_NUM[""+i] = i;
}
HEX_VAL_TO_NUM["A"] = 10;
HEX_VAL_TO_NUM["B"] = 11;
HEX_VAL_TO_NUM["C"] = 12;
HEX_VAL_TO_NUM["D"] = 13;
HEX_VAL_TO_NUM["E"] = 14;
HEX_VAL_TO_NUM["F"] = 15;
HEX_VAL_TO_NUM["a"] = 10;
HEX_VAL_TO_NUM["b"] = 11;
HEX_VAL_TO_NUM["c"] = 12;
HEX_VAL_TO_NUM["d"] = 13;
HEX_VAL_TO_NUM["e"] = 14;
HEX_VAL_TO_NUM["f"] = 15;

/**
 * 
 * @param {int} x A number in base 10
 * @returns A hex string corresponding to x 
 */
function base10ToHex(x) {
    let rem = x;
    let b = "";
    let place = 16;
    do {
        let val = (rem%place)/(place/16);
        b = HEX_VALS[val] + b;
        rem -= rem%place;
        place *= 16;
    }
    while (rem > 0);
    return b;
}

/**
 * 
 * @param {string} h A hex string
 * @returns An int corresponding to this hex string
 */
function hexToBase10(h) {
    let s = h.split("").reverse().join("");
    let place = 1;
    let x = 0;
    for (let i = 0; i < s.length; i++) {
        x += HEX_VAL_TO_NUM[s[i]]*place;
        place *= 16;
    }
    return x;
}

/**
 * 
 * @param {string} h A hex string
 * @returns HTML code for a table showing how to convert this to base 10
 */
function makeHexTableStr(h) {
    let s = "";
    s += "<table border = 1 cellpadding=10><tr>";
    let place = Math.pow(16, h.length-1);
    for (let i = 0; i < h.length; i++) {
        s += "<td><h3>" + place + "</h3></td>";
        place /= 16;
    }
    s += "</tr><tr>";
    for (let i = 0; i < h.length; i++) {
        s += "<td><h3>" + h[i] + "</h3></td>";
    }
    s += "</tr></table>";
    return s;
}

/**
 * 
 * @param {string} h A hex string
 * @returns HTML code showing how to sum up places to convert this
 *          to base 10
 */
function makeShowHexSumStr(h) {
    let x = hexToBase10(h);
    let s = "<h2>";
    let place = Math.pow(16, h.length-1);
    let hasLetters = false;
    for (let i = 0; i < h.length; i++) {
        if (HEX_VAL_TO_NUM[h[i]] > 9) {
            hasLetters = true;
        }
        s += "<font color=red>" + h[i] + "</font>*<font color=green>" + place+"</font>";
        if (i < h.length - 1) {
            s += "+ ";
        }
        else {
            s += " = ";
        }
        place /= 16;
    }
    s + "</code><BR>"
    s += "<b>" + x + "</b></h2>";

    // If there are letters in it, show an extra line to convert
    // the letters to numbers
    if (hasLetters) {
        s += "In other words...<h2>"
        place = Math.pow(16, h.length-1);
        for (let i = 0; i < h.length; i++) {
            s += "<font color=red>" + HEX_VAL_TO_NUM[h[i]] + "</font>*<font color=green>" + place+"</font>";
            if (i < h.length - 1) {
                s += "+ ";
            }
            else {
                s += " = ";
            }
            place /= 16;
        }
        s + "</code><BR>"
        s += "<b>" + x + "</b></h2><BR>";
    }
    return s;
}






/**
 * 
 * @param {string} b A binary string
 * @returns The corresponding hext string
 */
function binaryToHex(b) {
    let x = binaryToBase10(b);
    return base10ToHex(x);
}

/**
 * 
 * @param {string} h A hex string
 * @returns The corresponding binary string
 */
function hexToBinary(h) {
    let x = hexToBase10(h);
    return base10ToBinary(x);
}

/**
 * 
 * @param {string} h A hex string
 * @returns A string with HTML code to create a table showing
 *          how to convert each hexadecimal digit to bits
 *          4 bits at a time 
 */
function makeHexBinaryTableStr(h) {
    let s = "";
    s += "<table border = 1 cellpadding=10><tr>";
    for (let i = 0; i < h.length; i++) {
        s += "<td><h3>" + h[i] + "</h3></td>";
    }
    s += "</tr><tr>";
    for (let i = 0; i < h.length; i++) {
        s += "<td><h3>";
        let b = hexToBinary(h[i]);
        for (let j = 0; j < 4-b.length; j++) {
            s += "0";
        }
        for (let j = 0; j < b.length; j++) {
            s += b[j];
        }
        s += "</h3></td>";
    }
    s += "</tr></table>";
    return s;
}


/**
 * Make a table row string for a particular binary number
 * @param {string} The binary string to output
 * @param {string} startCell What to put in the first cell, if anything
 */
function makeBinaryTableRowStr(num, startCell) {
    if (startCell === undefined) {
        startCell = "";
    }
    let s = "<tr><td>" + startCell + "</td>";
    for (let i = 0; i < num.length; i++) {
        s += "<td><h2>&nbsp&nbsp"+num[i]+"&nbsp&nbsp</h2></td>";
    }
    s += "</tr>";
    return s;
}


/**
 * Do the OR of two bits
 * @param {int} xi First bit
 * @param {int} yi Second bit
 * @returns string of "0" or "1"
 */
function getORResult(xi, yi) {
    let result = "";
    if (xi == 1 || yi == 1) {
        result = "1";
    }
    else {
        result = "0";
    }
    return result;
}

/**
 * Do the AND of two bits
 * @param {int} xi First bit
 * @param {int} yi Second bit
 * @returns string of "0" or "1"
 */
function getANDResult(xi, yi) {
    let result = "";
    if (xi*yi == 1) {
        result = "1";
    }
    else {
        result = "0";
    }
    return result;
}

/**
 * Do the OR of two bits
 * @param {int} xi First bit
 * @param {int} yi Second bit
 * @returns string of "0" or "1"
 */
function getXORResult(xi, yi) {
    let result = "";
    if ((xi+yi)%2 == 1) {
        result = "1";
    }
    else {
        result = "0";
    }
    return result;
}


/**
 * Do a bitwise operation on x and y
 * @param {string} x First bit string
 * @param {string} y Second bit string
 * @param {function} fn Handle to a function which
 *                      operates on each pair of bits
 * @returns Resulting bit string
 */
function doBitwiseOP(x, y, fn) {
    // First, make sure the strings are the same length
    // Zeropad if not
    let N = Math.max(x.length, y.length);
    while(x.length < N) {
        x = "0" + x;
    }
    while (y.length < N) {
        y = "0" + y;
    }
    // Now go bit by bit and do the operation
    let result = "";
    for (let i = 0; i < x.length; i++) {
        let xi = parseInt(x[i]);
        let yi = parseInt(y[i]);
        result += fn(xi, yi);
    }
    return result;
}

/**
 * Do the binary AND of x and y
 * @param {string} x First bit string
 * @param {string} y Second bit string
 * @returns Resulting bit string
 */
function doBinaryAND(x, y) {
    return doBitwiseOP(x, y, getANDResult);
}


/**
 * Do the binary OR of x and y
 * @param {string} x First bit string
 * @param {string} y Second bit string
 * @returns Resulting bit string
 */
function doBinaryOR(x, y) {
    return doBitwiseOP(x, y, getORResult);
}

/**
 * Do the binary XOR of x and y
 * @param {string} x First bit string
 * @param {string} y Second bit string
 * @returns Resulting bit string
 */
function doBinaryXOR() {
    return doBitwiseOP(x, y, getXORResult);
}