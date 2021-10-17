import { Component, Input, OnInit } from '@angular/core';
import { BsModalService, BsModalRef } from 'ngx-bootstrap/modal';
import { FormControl } from '@angular/forms';

@Component({
  selector: 'components-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.scss']
})
export class ProductComponent implements OnInit {

  @Input() product: any;

  modalRef: BsModalRef | undefined;

  name = new FormControl('');
  formData = {
    product: null,
    delivery_start: null,
    delivery_date: null,
    entity:null,
    status: null,
  }
  // "product": 1,
  //   "delivery_start": "2021-10-18T20:20:50.928908Z",
  //   "delivery_date":"2021-10-18T20:20:50.928908Z",
  //   "entity": 14,
  //   "status": 2

  constructor(
    private modalService: BsModalService
  ) { }

  ngOnInit(): void {
    this.formData={
      product: this.product.id,
      delivery_start: null,
      delivery_date: null,
      entity:null,
      status: null,
    };
  }

  openModal(template: any){
    this.modalRef = this.modalService.show(template,
      {
        class: 'modal-dialogue-centered modal-md',
        backdrop: 'static',
        keyboard: false
      })
  }
  
  closeModal(){
    this.modalRef?.hide()
  }

  Order(){
    console.log(this.formData)
  }
}
