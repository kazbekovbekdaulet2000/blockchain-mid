// http://127.0.0.1:8000/market/sign-in/
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { ListGeneric } from '../models/list.model';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  URL = environment.URL

  constructor(
    protected http: HttpClient
  ) { }

  login(data: any): Observable<any>{
    return this.http.post<any>(`${this.URL}market/sign-in/`, data)
  }

  refresh(refresh: string): Observable<any>{
    return this.http.post<any>(`${this.URL}market/sign-in/refresh/`, {refresh: refresh})
  }

  register(data: any): Observable<any>{
    return this.http.post<any>(`${this.URL}market/sign-up/`, data)
  }
}
