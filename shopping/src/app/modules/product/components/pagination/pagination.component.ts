import { Component, OnInit } from '@angular/core';
import { ProductClientService } from 'src/app/shared/services/client/product-client.service';

@Component({
  selector: 'app-pagination',
  templateUrl: './pagination.component.html',
  styleUrls: ['./pagination.component.css']
})
export class PaginationComponent implements OnInit {
  optionsPerPage = [10, 20, 40, 50];
  constructor(private productClient: ProductClientService) { }

  ngOnInit(): void {
  }

  onChangePerPage(event: Event) {
    let perPage = Number.parseInt((event.target as HTMLSelectElement).value);
    let currentFilter = this.productClient.filterProduct$.getValue();
    this.productClient.filterProduct$.next({ ...currentFilter, perPage });
  }

}
