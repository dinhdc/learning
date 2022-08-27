import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-cart-status',
  templateUrl: './cart-status.component.html',
  styleUrls: ['./cart-status.component.css']
})
export class CartStatusComponent implements OnInit {
  totalPrice = 0;
  totalItems = 0;
  constructor() { }

  ngOnInit(): void {
  }

}
