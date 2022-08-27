import { Component, OnInit } from '@angular/core';
import { Event } from '@angular/router';
import { ProductClientService } from '../../services/client/product-client.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {
  searchKey: string = "";
  constructor(private productClient: ProductClientService) { }

  ngOnInit(): void {
  }

  onSubmitSearch() {
    let filter = this.productClient.filterProduct$.getValue();
    this.productClient.filterProduct$.next({ ...filter, name: this.searchKey });
  }

}
