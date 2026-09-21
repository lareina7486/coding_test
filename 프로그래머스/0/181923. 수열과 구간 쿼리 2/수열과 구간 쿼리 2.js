function solution(arr, queries) {
    let answer = [];
    let tempArr = [];
    queries.forEach(([s, e, k]) => {
        tempArr = arr.slice(s, e + 1).filter(n => n > k);
        answer.push(tempArr.length === 0 ? -1 : Math.min(...tempArr));
    });
    return answer;
}