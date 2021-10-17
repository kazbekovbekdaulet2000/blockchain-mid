import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { ListGeneric } from '../models/list.model';

@Injectable({
  providedIn: 'root'
})
export class ProductService {

  URL = environment.URL

  constructor(
    protected http: HttpClient
  ) { }

  list(params: any): Observable<ListGeneric<any>>{
    return this.http.get<ListGeneric<any>>(`${this.URL}market/products/`, {params})
  }

  orders(params: any): Observable<ListGeneric<any>>{
    return this.http.get<ListGeneric<any>>(`${this.URL}market/order/`, {params})
  }
}
