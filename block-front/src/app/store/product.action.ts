import { Injectable } from '@angular/core';
import { State } from '@ngxs/store';
import { Action } from 'rxjs/internal/scheduler/Action';
import { GetProductList } from './product.store';

@State<string[]>(
  {  
    name: 'Product',  
    defaults: []
  }
)
  
@Injectable()
export class ProductState {

}