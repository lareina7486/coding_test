function solution(num_list) {
    const odds = num_list.filter( value => value % 2 );
    const evens = num_list.filter( value => value % 2 === 0 );
    
    return Number(odds.join('')) + Number(evens.join(''));
}