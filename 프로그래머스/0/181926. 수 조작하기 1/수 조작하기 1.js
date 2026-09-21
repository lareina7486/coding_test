function solution(n, control) {
    for (const ch of control) {
  if (ch === 'w') n += 1;
  else if (ch === 's') n -= 1;
  else if (ch === 'd') n += 10;
  else n -= 10;
}
return n;
}