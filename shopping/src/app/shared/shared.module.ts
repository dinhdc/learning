import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeaderComponent } from './components/header/header.component';
import { CartStatusComponent } from './components/cart-status/cart-status.component';
import { FooterComponent } from './components/footer/footer.component';
import { SidebarComponent } from './components/sidebar/sidebar.component';
import {FormsModule} from '@angular/forms'


@NgModule({
  declarations: [
    HeaderComponent,
    CartStatusComponent,
    FooterComponent,
    SidebarComponent
  ],
  imports: [
    CommonModule,
    FormsModule
  ],
  exports: [
    HeaderComponent,
    CartStatusComponent,
    FooterComponent,
    SidebarComponent
  ]
})
export class SharedModule { }
