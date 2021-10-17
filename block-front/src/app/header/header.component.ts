import { Component, HostListener, Input, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'shared-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {
  @Input()
  height:number = 0

  constructor(
    private activetedroute: ActivatedRoute,
    private router: Router) { }

  ngOnInit(): void {
    
  }

  vh(v:number) {
    var h = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);
    return (v * h)/100;
  }
  
  currentPosition = window.pageXOffset;
  @HostListener("window:scroll", [])
  onWindowScroll() {
    const verticalOffset = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;
    if(0 > verticalOffset || verticalOffset > this.vh(this.height)){
      document.getElementsByClassName('header')[0].classList.add('background')
    }else{
      document.getElementsByClassName('header')[0].classList.remove('background')
    }
  }

}
