function longestCommonPrefix(strs: string[]) {
    let x = strs[0];
    let output = ""

    for(let i = 0; i < x.length; i++) {
        for (let j = 1; j < strs.length; j++) {
            if(strs[j].length < i) return output;
            if(strs[j][i] !== x[i]) return output;
            else continue;
        }
        output += x[i];
    }
    return output;
};