import { Component, OnInit } from '@angular/core';
import { ProductService } from '../core/services/product.service';

@Component({
  selector: 'app-order-list',
  templateUrl: './order-list.component.html',
  styleUrls: ['./order-list.component.scss']
})
export class OrderListComponent implements OnInit {

  list: any;

  constructor(
    private productService: ProductService
  ) { }

  ngOnInit(): void {
    this.productService.orders({}).subscribe(data=>{
      console.log(data)
      data.results.forEach(val=>{
          switch(val.status){
            case 0:
              val.status = "на комплектации"
              val.color = "blue"
              break;
            case 1: 
              val.status = "в пути" 
              val.color = "orange"
              break;
            case 2: 
              val.status ="доставлен"  
              val.color = "green"
              break; 
          }
        }
      )
      this.list = data.results
    })
  }

}
