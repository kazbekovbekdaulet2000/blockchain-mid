import { Component, OnInit } from '@angular/core';
import { ListGeneric } from '../core/models/list.model';
import { ProductService } from '../core/services/product.service';

@Component({
  selector: 'app-home-screen',
  templateUrl: './home-screen.component.html',
  styleUrls: ['./home-screen.component.scss']
})
export class HomeScreenComponent implements OnInit {

  list: ListGeneric<any> | undefined;

  constructor(
    private productService: ProductService
  ) { }

  ngOnInit(): void {
    this.getProducts()
  }

  getProducts(){
    this.productService.list({}).subscribe(data=>{
      this.list = data
    })
  }

}
