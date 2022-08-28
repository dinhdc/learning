import { IProduct } from "./product.interface";

export interface CartItem {
  product: IProduct;
  qty: number;
}

export interface ICartStatus {
  totalPrice: number;
  totalItems: number
}
