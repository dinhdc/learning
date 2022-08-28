import { Component, OnInit } from '@angular/core';
import { CartStatusService } from '../../services/client/cart-status.service';

@Component({
  selector: 'app-cart-status',
  templateUrl: './cart-status.component.html',
  styleUrls: ['./cart-status.component.css']
})
export class CartStatusComponent implements OnInit {
  totalPrice = 0;
  totalItems = 0;
  constructor(public cs: CartStatusService) { }

  ngOnInit(): void {
  }

}
