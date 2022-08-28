import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { CartItem, ICartStatus, IProduct } from '../../interfaces';

@Injectable({
  providedIn: 'root'
})
export class CartStatusService {

  carts: CartItem[] = [];
  cartStatus: BehaviorSubject<ICartStatus> = new BehaviorSubject<ICartStatus>({ totalItems: 0, totalPrice: 0 })

  constructor() { }

  addToCart(product: IProduct) {
    let index = this.carts.findIndex(c => c.product.id === product.id);
    if (index > -1) {
      this.carts[index].qty += 1;
    } else {
      this.carts.push({ product, qty: 1 });
    }
    this.updateCartStatus(product.unitPrice, 1);
  }

  updateCartStatus(price: number, qty: number) {
    let currentStatus = this.cartStatus.getValue();
    let totalPrice = currentStatus.totalPrice;
    currentStatus.totalItems += qty;
    totalPrice += price * qty;
    totalPrice = Number(totalPrice.toFixed(2));
    currentStatus.totalPrice = totalPrice;
    this.cartStatus.next(currentStatus);
  }
}
