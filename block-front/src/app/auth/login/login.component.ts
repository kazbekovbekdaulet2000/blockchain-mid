import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/core/services/auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  public user = {}
  constructor(
    private route: Router,
    private auth: AuthService
  ) { }
  
  userinfo = {} as any;
  userJWT = {} as any;

  ngOnInit(): void {
  }

  login(){
    this.auth.login(this.userinfo).subscribe(
      res=>{
        localStorage.setItem('access', res.access)
        localStorage.setItem('refresh', res.refresh)
        this.route.navigate([''])
      },
      err=>{
        alert("Неправильный логин или пароль")
      }
      )
  }

}
