import { CartStatusService } from './../../../../shared/services/client/cart-status.service';
import { IProduct } from 'src/app/shared/interfaces/product.interface';
import { Component, OnInit } from '@angular/core';
import { ProductService } from 'src/app/shared/services/server/product.service';
import { ActivatedRoute } from '@angular/router';
@Component({
  selector: 'app-product-detail',
  templateUrl: './product-detail.component.html',
  styleUrls: ['./product-detail.component.css']
})
export class ProductDetailComponent implements OnInit {

  constructor(private ps: ProductService, private ar: ActivatedRoute, private cs: CartStatusService) { }

  product!: IProduct;

  ngOnInit(): void {
    let productId = Number.parseInt(this.ar.snapshot.paramMap.get('id') || '1');
    this.ps.getProductDetail(productId).subscribe(product => this.product = product);
  }

  addToCart(){
    this.cs.addToCart(this.product);
  }

}
