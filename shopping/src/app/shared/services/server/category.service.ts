import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { ICategory } from 'src/app/shared/interfaces/category.interface';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class CategoryService {

  private baseUrl = environment.URL;

  constructor(private http: HttpClient) { }

  getCategoryList() {
    return this.http.get<ICategory[]>(`${this.baseUrl}/api/categories`);
  }
}
