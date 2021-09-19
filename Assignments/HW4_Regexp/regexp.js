function problem1(regexp) {
    let re = new RegExp('^(' + regexp + ')$');
    let table = document.getElementById("problem1res");
    table.innerHTML = "<tr><td>Input</td><td>Expected Result</td><td>Your Result</td></tr>";
    let tests = ["aba", "abaa", "aaaccaaba", "abacccaa", "bbbaaaab","abaccaa", "bbbaabbb", "abbabbbabbaaaaab"];
    for (let i = 0; i < tests.length; i++) {
        const test = tests[i];
        let tr = document.createElement("tr");
        let td = document.createElement("td");
        td.innerHTML = test;
        tr.appendChild(td);
        let res = re.test(test);

        let as = 0;
        let cs = 0;
        for (let k = 0; k < test.length; k++) {
            if (test[k] == "a") {
                as += 1;
            }
            else if (test[k] == "c") {
                cs += 1;
            }
        }
        let gtres = as%2 == 0 && (cs == 0 || cs == 0);
        td = document.createElement("td");
        td.innerHTML = gtres;
        tr.appendChild(td);

        td = document.createElement("td");
        let span = document.createElement("span");
        if (res == gtres) {
            span.setAttribute("style", "color:green");
        }
        else {
            span.setAttribute("style", "color:red");
        }
        span.innerHTML = res;
        td.appendChild(span);
        tr.appendChild(td);
        table.appendChild(tr);
    }
}

function clearProblem1() {
    let table = document.getElementById("problem1res");
    table.innerHTML = "";
}








function problem2(regexp) {
    let re = new RegExp('^(' + regexp + ')$');
    let table = document.getElementById("problem2res");
    table.innerHTML = "<tr><td>Input</td><td>Expected Result</td><td>Your Result</td></tr>";
    let tests = ["abcabcaa", "ababcbca", "aaaaabcaaa", "bbbbb", "cccc", "acabacab", "aaaaa"];
    for (let i = 0; i < tests.length; i++) {
        const test = tests[i];
        let tr = document.createElement("tr");
        let td = document.createElement("td");
        td.innerHTML = test;
        tr.appendChild(td);
        let res = re.test(test);

        let bs = 0;
        let cs = 0;
        for (let k = 0; k < test.length; k++) {
            if (test[k] == "b") {
                bs += 1;
            }
            else if (test[k] == "c") {
                cs += 1;
            }
        }
        let gtres = (bs + cs == 4);
        td = document.createElement("td");
        td.innerHTML = gtres;
        tr.appendChild(td);

        td = document.createElement("td");
        let span = document.createElement("span");
        if (res == gtres) {
            span.setAttribute("style", "color:green");
        }
        else {
            span.setAttribute("style", "color:red");
        }
        span.innerHTML = res;
        td.appendChild(span);
        tr.appendChild(td);
        table.appendChild(tr);
    }
}

function clearProblem2() {
    let table = document.getElementById("problem2res");
    table.innerHTML = "";
}









function problem3(regexp) {
    let re = new RegExp('^(' + regexp + ')$');
    let table = document.getElementById("problem3res");
    table.innerHTML = "<tr><td>Decimal</td><td>Binary</td><td>Reported Div By 5</td></tr>";
    for (let i = 0; i <= 4000; i++) {
        let tr = document.createElement("tr");
        let td = document.createElement("td");
        td.innerHTML = i;
        tr.appendChild(td);
        let s = i.toString(2);
        td = document.createElement("td");
        td.innerHTML = s;
        tr.appendChild(td);
        let res = re.test(s);
        if (res || i%5 == 0) {
            td = document.createElement("td");
            let span = document.createElement("span");
            if (i%5 == 0 && res) {
                span.setAttribute("style", "color:green");
            }
            else {
                span.setAttribute("style", "color:red");
            }
            span.innerHTML = res;
            td.appendChild(span);
            tr.appendChild(td);
            table.appendChild(tr);
        }
    }
}

function clearProblem3() {
    let table = document.getElementById("problem3res");
    table.innerHTML = "";
}