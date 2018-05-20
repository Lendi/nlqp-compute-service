import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';
  query = '';
  constructor(private http: HttpClient){
  }

  onEnter(value: string) {
    this.query = value;
    this.http.get('http://localhost:5000/api/v1/query/'+this.query).subscribe(data => {
      console.log(data);
    });
  }

}
