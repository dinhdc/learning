import { IFilterProduct } from './../../interfaces/product.interface';
import { IProduct, ProductListResponse } from 'src/app/shared/interfaces/product.interface';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ProductService {

  private baseUrl = environment.URL;

  constructor(private http: HttpClient) { }

  getProductList(filter: IFilterProduct) {
    let query = '?';
    if(filter.name){
      query += 'name='+filter.name;
    }
    if(filter.category){
      query += '&category='+filter.category;
    }
    if(filter.page){
      query += '&page='+filter.page;
    }
    if(filter.perPage){
      query += '&perPage='+filter.perPage;
    }
    return this.http.get<ProductListResponse>(`${this.baseUrl}/api/products${query}`);
  }
}


