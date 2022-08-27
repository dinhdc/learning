export interface IProduct {
  id: number;
  category: string;
  sku: string;
  name: string;
  description: string;
  unitPrice: number;
  image: string;
  active: boolean;
  unitsInStock: number;
  createdAt: Date;
  updatedAt: Date;
}

export interface ProductListResponse{
  data: IProduct[];
  previous: boolean;
  next: boolean;
}

export interface IFilterProduct{
  name?: string;
  category?: number;
  page: number;
  perPage: number;
}
