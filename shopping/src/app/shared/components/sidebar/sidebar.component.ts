import { ProductClientService } from './../../services/client/product-client.service';
import { Component, OnInit } from '@angular/core';
import { ICategory } from '../../interfaces/category.interface';
import { CategoryService } from '../../services/server/category.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent implements OnInit {
  categories: ICategory[] = []
  constructor(private router: Router, private categoryService: CategoryService, private productClient: ProductClientService) { }

  ngOnInit(): void {
    this.categoryService.getCategoryList().subscribe(data => this.categories = data)
  }

  navigateHomePage() {
    this.productClient.setDefaultFilter();
    this.router.navigate(["/"]);
  }

  onFilterCategory(id: number){
    let currentFilter = this.productClient.filterProduct$.getValue();
    this.productClient.filterProduct$.next({...currentFilter, category: id});
  }

}
