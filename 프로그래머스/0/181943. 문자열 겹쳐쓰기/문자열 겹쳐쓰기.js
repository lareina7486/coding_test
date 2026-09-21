function solution(my_string, overwrite_string, s) {
    ansArr = my_string.split('');
    ansArr.splice(s, overwrite_string.length, overwrite_string); 
    return ansArr.join('');
}