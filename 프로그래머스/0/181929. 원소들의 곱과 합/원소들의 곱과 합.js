function solution(num_list) {
    let sum = 0;
    let mul = 1;
    num_list.forEach( value => {
      sum+=value;
      mul*=value;
    });
    return (sum*sum > mul) ? 1 : 0;
}