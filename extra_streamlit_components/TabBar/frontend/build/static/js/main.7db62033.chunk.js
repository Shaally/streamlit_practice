(this.webpackJsonptab_bar=this.webpackJsonptab_bar||[]).push([[0],{16:function(e,t,a){e.exports=a(24)},24:function(e,t,a){"use strict";a.r(t);var r=a(6),n=a.n(r),c=a(13),l=a.n(c),s=a(0),o=a(3),i=a(1),u=a(2),d=a(11),m=a(15),f=a.n(m),p=function(e){Object(i.a)(a,e);var t=Object(u.a)(a);function a(e){var r;return Object(s.a)(this,a),(r=t.call(this,e)).state={numClicks:0,selectedId:1,list:[]},r.MenuItem=function(e){var t=e.item,a=e.selectedId;return n.a.createElement("div",{className:"menu-item ".concat(a==t.id?"active":"")},n.a.createElement("div",null,t.title),n.a.createElement("div",{style:{fontWeight:"normal",fontStyle:"italic"}},t.description))},r.Arrow=function(e){var t=e.text,a=e.className;return n.a.createElement("div",{className:a},t)},r.ArrowLeft=r.Arrow({text:"<",className:"arrow-prev"}),r.ArrowRight=r.Arrow({text:">",className:"arrow-next"}),r.render=function(){return n.a.createElement("div",null,n.a.createElement(f.a,{alignCenter:!1,data:r.Menu(r.state.list,r.state.selectedId),wheel:!0,scrollToSelected:!0,selected:"".concat(r.state.selectedId),onSelect:r.onSelect}),n.a.createElement("hr",{style:{borderColor:"var(--streamlit-primary-color)"}}))},r.onSelect=function(e){r.setState((function(t,a){return{selectedId:e}}),(function(){return d.a.setComponentValue(e)}))},r.state.list=r.props.args.data,r.state.selectedId=r.props.args.selectedId,r}return Object(o.a)(a,[{key:"Menu",value:function(e,t){var a=this;return e.map((function(e){return n.a.createElement(a.MenuItem,{item:e,selectedId:t,key:e.id})}))}}]),a}(d.b),v=Object(d.c)(p);l.a.render(n.a.createElement(n.a.StrictMode,null,n.a.createElement(v,null)),document.getElementById("root"))}},[[16,1,2]]]);
//# sourceMappingURL=main.7db62033.chunk.js.map