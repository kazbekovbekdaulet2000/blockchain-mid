export interface ListGeneric<T>{
  count: number,
  next: string,
  previous: string,
  results: [T]
}