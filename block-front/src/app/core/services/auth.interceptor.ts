import { Injectable } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor,
  HttpClient
} from '@angular/common/http';
import { Observable } from 'rxjs';
import { Router } from '@angular/router';
import { environment } from 'src/environments/environment';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {
    
  constructor(
    private router: Router,
  ) {}


  URL = environment.URL

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    const access = localStorage.getItem('access');
    if (access){
        req = req.clone({
          setHeaders: {
            'Authorization': `Bearer ${access}`
          }
        });
    }else{
      this.router.navigate(['login'])
    }
    return next.handle(req)
  }
}
