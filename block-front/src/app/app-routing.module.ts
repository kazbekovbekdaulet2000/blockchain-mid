import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { component } from 'vue/types/umd';
import { LoginComponent } from './auth/login/login.component';
import { HomeScreenComponent } from './home-screen/home-screen.component';
import { ProductDetailComponent } from './home-screen/product-detail/product-detail.component';
import { OrderListComponent } from './order-list/order-list.component';

const routes: Routes = [
  {path:'', component: HomeScreenComponent},
  {path:'detail/:id', component: ProductDetailComponent},
  {path:'orders', component: OrderListComponent},
  {path:'login', component: LoginComponent},
  {path:'sign-up', component: LoginComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
