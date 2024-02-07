const sq = x => x * x;

const sqSum = (x, y) => sq(x) + sq(y);

export const hypotenuse = (a, b) => Math.sqrt(sqSum(a, b))

export const perimeter = (a, b, c) => a + b + c;

export const area = (a, b, c) => {
  const s = (a + b + c) / 2;
  return Math.sqrt(s * (s - a) * (s - b) * (s - c));
}