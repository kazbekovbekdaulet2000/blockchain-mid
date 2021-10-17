import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';

import { NgxsModule } from '@ngxs/store';
import { HomeScreenComponent } from './home-screen/home-screen.component';
import { ProductDetailComponent } from './home-screen/product-detail/product-detail.component';
import { ProductState } from './store/product.action';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ProductComponent } from './home-screen/product/product.component';
import { LoginComponent } from './auth/login/login.component';
import { ModalModule } from 'ngx-bootstrap/modal';
import { AuthInterceptor } from './core/services/auth.interceptor';
import { OrderListComponent } from './order-list/order-list.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    HomeScreenComponent,
    ProductDetailComponent,
    ProductComponent,
    LoginComponent,
    OrderListComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    FormsModule,
    HttpClientModule,
    ModalModule.forRoot(),
    NgxsModule.forRoot([ProductState])
  ],
  providers: [
    { provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
