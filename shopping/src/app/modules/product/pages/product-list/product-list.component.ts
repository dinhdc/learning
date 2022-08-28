import { ProductClientService } from './../../../../shared/services/client/product-client.service';
import { IFilterProduct } from './../../../../shared/interfaces/product.interface';
import { IProduct } from 'src/app/shared/interfaces/product.interface';
import { Component, OnInit } from '@angular/core';
import { ProductService } from 'src/app/shared/services/server/product.service';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit {

  products: IProduct[] = [];
  optionsPerPage = [10, 20, 40, 50]

  constructor(private productService: ProductService, private productClient: ProductClientService) { }

  ngOnInit(): void {
    this.productClient.filterProduct$.subscribe(filter => {
      this.getListProduct(filter);
    })
  }

  getListProduct(filter: IFilterProduct) {
    this.productService.getProductList(filter).subscribe(res => {
      this.products = res.data;
      this.productClient.nextPage$.next(res.next);
      this.productClient.previousPage$.next(res.previous);
    });
  }

}
