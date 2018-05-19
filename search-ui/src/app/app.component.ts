import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';
  query = '';
  onEnter(value: string) {
    // TODO: Replace this with an ajax call to compute service to query
    this.query = value;
  }
}
