import { CartStatusService } from './../../../../shared/services/client/cart-status.service';
import { Component, Input, OnInit } from '@angular/core';
import { IProduct } from 'src/app/shared/interfaces/product.interface';

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent implements OnInit {
  @Input("product") p!: IProduct;
  constructor(private cs: CartStatusService) { }

  ngOnInit(): void {
  }

  addToCart(){
    this.cs.addToCart(this.p);
  }

}
