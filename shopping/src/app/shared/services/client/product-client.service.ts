import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { IFilterProduct } from '../../interfaces/product.interface';

@Injectable({
  providedIn: 'root'
})
export class ProductClientService {

  defaultFilter: IFilterProduct = {
    name: '',
    category: undefined,
    page: 1,
    perPage: 10
  }

  filterProduct$: BehaviorSubject<IFilterProduct> = new BehaviorSubject<IFilterProduct>(this.defaultFilter);
  constructor() { }

  setDefaultFilter(){
    this.filterProduct$.next(this.defaultFilter);
  }
}
