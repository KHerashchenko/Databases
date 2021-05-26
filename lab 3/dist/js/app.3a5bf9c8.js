(function(t){function e(e){for(var o,n,d=e[0],s=e[1],c=e[2],l=0,u=[];l<d.length;l++)n=d[l],Object.prototype.hasOwnProperty.call(a,n)&&a[n]&&u.push(a[n][0]),a[n]=0;for(o in s)Object.prototype.hasOwnProperty.call(s,o)&&(t[o]=s[o]);m&&m(e);while(u.length)u.shift()();return i.push.apply(i,c||[]),r()}function r(){for(var t,e=0;e<i.length;e++){for(var r=i[e],o=!0,d=1;d<r.length;d++){var s=r[d];0!==a[s]&&(o=!1)}o&&(i.splice(e--,1),t=n(n.s=r[0]))}return t}var o={},a={app:0},i=[];function n(e){if(o[e])return o[e].exports;var r=o[e]={i:e,l:!1,exports:{}};return t[e].call(r.exports,r,r.exports,n),r.l=!0,r.exports}n.m=t,n.c=o,n.d=function(t,e,r){n.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:r})},n.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},n.t=function(t,e){if(1&e&&(t=n(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var r=Object.create(null);if(n.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var o in t)n.d(r,o,function(e){return t[e]}.bind(null,o));return r},n.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return n.d(e,"a",e),e},n.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},n.p="/";var d=window["webpackJsonp"]=window["webpackJsonp"]||[],s=d.push.bind(d);d.push=e,d=d.slice();for(var c=0;c<d.length;c++)e(d[c]);var m=s;i.push([0,"chunk-vendors"]),r()})({0:function(t,e,r){t.exports=r("56d7")},"034f":function(t,e,r){"use strict";r("85ec")},"56d7":function(t,e,r){"use strict";r.r(e);r("e260"),r("e6cf"),r("cca6"),r("a79d");var o=r("5f5b"),a=r("2b0e"),i=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",{attrs:{id:"app"}},[r("b-navbar",{attrs:{toggleable:"lg",type:"dark",variant:"dark"}},[r("b-navbar-brand",{attrs:{to:"/actors"}},[t._v("Actors")]),r("b-navbar-brand",{attrs:{to:"/movies"}},[t._v("Movies")]),r("b-navbar-brand",{attrs:{to:"/directors"}},[t._v("Directors")])],1),r("router-view")],1)},n=[],d=(r("034f"),r("2877")),s={},c=Object(d["a"])(s,i,n,!1,null,null,null),m=c.exports,l=r("8c4f"),u=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",{staticClass:"container"},[r("div",{staticClass:"row"},[r("div",{staticClass:"col-sm-10"},[r("h1",[t._v("Actors")]),r("hr"),r("br"),r("br"),t.showMessage?r("alert",{attrs:{message:t.message}}):t._e(),r("button",{directives:[{name:"b-modal",rawName:"v-b-modal.actor-modal",modifiers:{"actor-modal":!0}}],staticClass:"btn btn-success btn-sm",attrs:{type:"button"}},[t._v("Add Actor")]),r("br"),r("br"),r("table",{staticClass:"table table-hover"},[t._m(0),r("tbody",t._l(t.actors,(function(e,o){return r("tr",{key:o},[r("td",[t._v(t._s(e.id))]),r("td",[t._v(t._s(e.name))]),r("td",[t._v(t._s(e.gender))]),r("td",[t._v(t._s(e.date_of_birth))]),r("td",[r("div",{staticClass:"btn-group",attrs:{role:"group"}},[r("button",{directives:[{name:"b-modal",rawName:"v-b-modal.actor-update-modal",modifiers:{"actor-update-modal":!0}}],staticClass:"btn btn-warning btn-sm",attrs:{type:"button"},on:{click:function(r){return t.editActor(e)}}},[t._v(" Update ")]),r("button",{staticClass:"btn btn-danger btn-sm",attrs:{type:"button"},on:{click:function(r){return t.onDeleteActor(e)}}},[t._v(" Delete ")])])])])})),0)])],1)]),r("b-modal",{ref:"addActorModal",attrs:{id:"actor-modal",title:"Add a new actor","hide-footer":""}},[r("b-form",{staticClass:"w-100",on:{submit:t.onSubmit,reset:t.onReset}},[r("b-form-group",{attrs:{id:"form-name-group",label:"Name:","label-for":"form-name-input"}},[r("b-form-input",{attrs:{id:"form-name-input",type:"text",required:"",placeholder:"Enter name"},model:{value:t.addActorForm.name,callback:function(e){t.$set(t.addActorForm,"name",e)},expression:"addActorForm.name"}})],1),r("b-form-group",{attrs:{id:"form-gender-group",label:"Gender:","label-for":"form-gender-input"}},[r("b-form-select",{attrs:{options:t.options},model:{value:t.addActorForm.gender,callback:function(e){t.$set(t.addActorForm,"gender",e)},expression:"addActorForm.gender"}})],1),r("b-form-group",{attrs:{id:"form-date-group",label:"Date of birth:","label-for":"form-date-input"}},[r("b-form-input",{attrs:{id:"form-date-input",type:"date",required:"",placeholder:"DD.MM.YYYY"},model:{value:t.addActorForm.date_of_birth,callback:function(e){t.$set(t.addActorForm,"date_of_birth",e)},expression:"addActorForm.date_of_birth"}})],1),r("b-button-group",[r("b-button",{attrs:{type:"submit",variant:"primary"}},[t._v("Submit")]),r("b-button",{attrs:{type:"reset",variant:"danger"}},[t._v("Reset")])],1)],1)],1),r("b-modal",{ref:"editActorModal",attrs:{id:"actor-update-modal",title:"Update","hide-footer":""}},[r("b-form",{staticClass:"w-100",on:{submit:t.onSubmitUpdate,reset:t.onResetUpdate}},[r("b-form-group",{attrs:{id:"form-name-edit-group",label:"ID:","label-for":"form-id-edit-input"}},[r("b-form-input",{attrs:{id:"form-id-edit-input",type:"text",required:"",placeholder:"Enter ID"},model:{value:t.editForm.id,callback:function(e){t.$set(t.editForm,"id",e)},expression:"editForm.id"}})],1),r("b-form-group",{attrs:{id:"form-name-edit-group",label:"Name:","label-for":"form-name-edit-input"}},[r("b-form-input",{attrs:{id:"form-name-edit-input",type:"text",required:"",placeholder:"Enter name"},model:{value:t.editForm.name,callback:function(e){t.$set(t.editForm,"name",e)},expression:"editForm.name"}})],1),r("b-form-group",{attrs:{id:"form-gender-edit-group",label:"Gender:","label-for":"form-gender-edit-input"}},[r("b-form-select",{attrs:{options:t.options},model:{value:t.editForm.gender,callback:function(e){t.$set(t.editForm,"gender",e)},expression:"editForm.gender"}})],1),r("b-form-group",{attrs:{id:"form-date-edit-group",label:"Date of birth:","label-for":"form-date-edit-input"}},[r("b-form-input",{attrs:{id:"form-date-input",type:"date",required:"",placeholder:"DD.MM.YYYY"},model:{value:t.editForm.date_of_birth,callback:function(e){t.$set(t.editForm,"date_of_birth",e)},expression:"editForm.date_of_birth"}})],1),r("b-button-group",[r("b-button",{attrs:{type:"submit",variant:"primary"}},[t._v("Update")]),r("b-button",{attrs:{type:"reset",variant:"danger"}},[t._v("Cancel")])],1)],1)],1)],1)},f=[function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("thead",[r("tr",[r("th",{attrs:{scope:"col"}},[t._v("ID")]),r("th",{attrs:{scope:"col"}},[t._v("Name")]),r("th",{attrs:{scope:"col"}},[t._v("Gender")]),r("th",{attrs:{scope:"col"}},[t._v("Date of birth")]),r("th")])])}],p=(r("b0c0"),r("bc3a")),b=r.n(p),h=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("b-alert",{attrs:{variant:"success",show:""}},[t._v(t._s(t.message))]),r("br")],1)},v=[],g={props:["message"]},_=g,F=Object(d["a"])(_,h,v,!1,null,null,null),M=F.exports,D={data:function(){return{options:[{value:null,text:"Please select a gender"},{value:"male",text:"Male"},{value:"female",text:"Female"}],actors:[],addActorForm:{name:"",gender:null,date_of_birth:""},message:"",showMessage:!1,editForm:{id:"",name:"",gender:"",date_of_birth:""}}},components:{alert:M},methods:{getActors:function(){var t=this,e="/api/actors";b.a.get(e).then((function(e){t.actors=e.data})).catch((function(t){console.error(t)}))},addActor:function(t){var e=this,r="/api/actor";b.a.post(r,t).then((function(){e.getActors(),e.message="actor added!",e.showMessage=!0})).catch((function(t){console.log(t),e.message=t,e.showMessage=!0,e.getActors()}))},initForm:function(){this.addDirectorForm.name="",this.addDirectorForm.gender=null,this.addDirectorForm.date_of_birth="",this.editForm.id="",this.editForm.name="",this.editForm.gender=null,this.editForm.date_of_birth=""},onSubmit:function(t){t.preventDefault(),this.$refs.addActorModal.hide();var e={name:this.addActorForm.name,gender:this.addActorForm.gender,date_of_birth:this.addActorForm.date_of_birth};this.addActor(e),this.initForm()},onReset:function(t){t.preventDefault(),this.$refs.addActorModal.hide(),this.initForm()},editActor:function(t){this.editForm=t},onSubmitUpdate:function(t){t.preventDefault(),this.$refs.editActorModal.hide();var e={id:this.editForm.id,name:this.editForm.name,gender:this.editForm.gender,date_of_birth:this.editForm.date_of_birth};this.updateActor(e)},updateActor:function(t){var e=this,r="/api/actor";b.a.put(r,t).then((function(){e.getActors(),e.message="actor updated!",e.showMessage=!0})).catch((function(t){console.error(t),e.getActors()}))},onResetUpdate:function(t){t.preventDefault(),this.$refs.editActorModal.hide(),this.initForm(),this.getActors()},removeActor:function(t){var e=this,r="/api/actor";b.a.delete(r,{data:t}).then((function(){e.getActors(),e.message="actor removed!",e.showMessage=!0})).catch((function(t){console.error(t),e.getActors()}))},onDeleteActor:function(t){var e={id:t.id};this.removeActor(e)}},created:function(){this.getActors()}},y=D,x=Object(d["a"])(y,u,f,!1,null,null,null),w=x.exports,A=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",{staticClass:"container"},[r("div",{staticClass:"row"},[r("div",{staticClass:"col-sm-10"},[r("h1",[t._v("Directors")]),r("hr"),r("br"),r("br"),t.showMessage?r("alert",{attrs:{message:t.message}}):t._e(),r("button",{directives:[{name:"b-modal",rawName:"v-b-modal.director-modal",modifiers:{"director-modal":!0}}],staticClass:"btn btn-success btn-sm",attrs:{type:"button"}},[t._v("Add Director")]),r("br"),r("br"),r("table",{staticClass:"table table-hover"},[t._m(0),r("tbody",t._l(t.directors,(function(e,o){return r("tr",{key:o},[r("td",[t._v(t._s(e.id))]),r("td",[t._v(t._s(e.name))]),r("td",[t._v(t._s(e.gender))]),r("td",[t._v(t._s(e.date_of_birth))]),r("td",[r("div",{staticClass:"btn-group",attrs:{role:"group"}},[r("button",{directives:[{name:"b-modal",rawName:"v-b-modal.director-update-modal",modifiers:{"director-update-modal":!0}}],staticClass:"btn btn-warning btn-sm",attrs:{type:"button"},on:{click:function(r){return t.editDirector(e)}}},[t._v(" Update ")]),r("button",{staticClass:"btn btn-danger btn-sm",attrs:{type:"button"},on:{click:function(r){return t.onDeleteDirector(e)}}},[t._v(" Delete ")])])])])})),0)])],1)]),r("b-modal",{ref:"addDirectorModal",attrs:{id:"director-modal",title:"Add a new director","hide-footer":""}},[r("b-form",{staticClass:"w-100",on:{submit:t.onSubmit,reset:t.onReset}},[r("b-form-group",{attrs:{id:"form-name-group",label:"Name:","label-for":"form-name-input"}},[r("b-form-input",{attrs:{id:"form-name-input",type:"text",required:"",placeholder:"Enter name"},model:{value:t.addDirectorForm.name,callback:function(e){t.$set(t.addDirectorForm,"name",e)},expression:"addDirectorForm.name"}})],1),r("b-form-group",{attrs:{id:"form-gender-group",label:"Gender:","label-for":"form-gender-input"}},[r("b-form-select",{attrs:{options:t.options},model:{value:t.addDirectorForm.gender,callback:function(e){t.$set(t.addDirectorForm,"gender",e)},expression:"addDirectorForm.gender"}})],1),r("b-form-group",{attrs:{id:"form-date-group",label:"Date of birth:","label-for":"form-date-input"}},[r("b-form-input",{attrs:{id:"form-date-input",type:"date",required:"",placeholder:"DD.MM.YYYY"},model:{value:t.addDirectorForm.date_of_birth,callback:function(e){t.$set(t.addDirectorForm,"date_of_birth",e)},expression:"addDirectorForm.date_of_birth"}})],1),r("b-button-group",[r("b-button",{attrs:{type:"submit",variant:"primary"}},[t._v("Submit")]),r("b-button",{attrs:{type:"reset",variant:"danger"}},[t._v("Reset")])],1)],1)],1),r("b-modal",{ref:"editDirectorModal",attrs:{id:"director-update-modal",title:"Update","hide-footer":""}},[r("b-form",{staticClass:"w-100",on:{submit:t.onSubmitUpdate,reset:t.onResetUpdate}},[r("b-form-group",{attrs:{id:"form-name-edit-group",label:"ID:","label-for":"form-id-edit-input"}},[r("b-form-input",{attrs:{id:"form-id-edit-input",type:"text",required:"",placeholder:"Enter ID"},model:{value:t.editForm.id,callback:function(e){t.$set(t.editForm,"id",e)},expression:"editForm.id"}})],1),r("b-form-group",{attrs:{id:"form-name-edit-group",label:"Name:","label-for":"form-name-edit-input"}},[r("b-form-input",{attrs:{id:"form-name-edit-input",type:"text",required:"",placeholder:"Enter name"},model:{value:t.editForm.name,callback:function(e){t.$set(t.editForm,"name",e)},expression:"editForm.name"}})],1),r("b-form-group",{attrs:{id:"form-gender-edit-group",label:"Gender:","label-for":"form-gender-edit-input"}},[r("b-form-select",{attrs:{options:t.options},model:{value:t.editForm.gender,callback:function(e){t.$set(t.editForm,"gender",e)},expression:"editForm.gender"}})],1),r("b-form-group",{attrs:{id:"form-date-edit-group",label:"Date of birth:","label-for":"form-date-edit-input"}},[r("b-form-input",{attrs:{id:"form-name-date-input",type:"date",required:"",placeholder:"DD.MM.YYYY"},model:{value:t.editForm.date_of_birth,callback:function(e){t.$set(t.editForm,"date_of_birth",e)},expression:"editForm.date_of_birth"}})],1),r("b-button-group",[r("b-button",{attrs:{type:"submit",variant:"primary"}},[t._v("Update")]),r("b-button",{attrs:{type:"reset",variant:"danger"}},[t._v("Cancel")])],1)],1)],1)],1)},$=[function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("thead",[r("tr",[r("th",{attrs:{scope:"col"}},[t._v("ID")]),r("th",{attrs:{scope:"col"}},[t._v("Name")]),r("th",{attrs:{scope:"col"}},[t._v("Gender")]),r("th",{attrs:{scope:"col"}},[t._v("Date of birth")]),r("th")])])}],k={data:function(){return{options:[{value:null,text:"Please select a gender"},{value:"male",text:"Male"},{value:"female",text:"Female"}],directors:[],addDirectorForm:{name:"",gender:null,date_of_birth:""},message:"",showMessage:!1,editForm:{id:"",name:"",gender:"",date_of_birth:""}}},components:{alert:M},methods:{getDirectors:function(){var t=this,e="/api/directors";b.a.get(e).then((function(e){t.directors=e.data})).catch((function(t){console.error(t)}))},addDirector:function(t){var e=this,r="/api/director";b.a.post(r,t).then((function(){e.getDirectors(),e.message="director added!",e.showMessage=!0})).catch((function(t){console.log(t),e.message=t,e.showMessage=!0,e.getDirectors()}))},initForm:function(){this.addDirectorForm.name="",this.addDirectorForm.gender=null,this.addDirectorForm.date_of_birth="",this.editForm.id="",this.editForm.name="",this.editForm.gender=null,this.editForm.date_of_birth=""},onSubmit:function(t){t.preventDefault(),this.$refs.addDirectorModal.hide();var e={name:this.addDirectorForm.name,gender:this.addDirectorForm.gender,date_of_birth:this.addDirectorForm.date_of_birth};this.addDirector(e),this.initForm()},onReset:function(t){t.preventDefault(),this.$refs.addDirectorModal.hide(),this.initForm()},editDirector:function(t){this.editForm=t},onSubmitUpdate:function(t){t.preventDefault(),this.$refs.editDirectorModal.hide();var e={id:this.editForm.id,name:this.editForm.name,gender:this.editForm.gender,date_of_birth:this.editForm.date_of_birth};this.updateDirector(e)},updateDirector:function(t){var e=this,r="/api/director";b.a.put(r,t).then((function(){e.getDirectors(),e.message="director updated!",e.showMessage=!0})).catch((function(t){console.error(t),e.getDirectors()}))},onResetUpdate:function(t){t.preventDefault(),this.$refs.editDirectorModal.hide(),this.initForm(),this.getDirectors()},removeDirector:function(t){var e=this,r="/api/director";b.a.delete(r,{data:t}).then((function(){e.getDirectors(),e.message="director removed!",e.showMessage=!0})).catch((function(t){console.error(t),e.getDirectors()}))},onDeleteDirector:function(t){var e={id:t.id};this.removeDirector(e)}},created:function(){this.getDirectors()}},C=k,E=Object(d["a"])(C,A,$,!1,null,null,null),U=E.exports,S=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",{staticClass:"container"},[r("div",{staticClass:"row"},[r("div",{staticClass:"col-sm-10"},[r("h1",[t._v("Movies")]),r("hr"),r("br"),r("br"),t.showMessage?r("alert",{attrs:{message:t.message}}):t._e(),r("button",{directives:[{name:"b-modal",rawName:"v-b-modal.movie-modal",modifiers:{"movie-modal":!0}}],staticClass:"btn btn-success btn-sm",attrs:{type:"button"}},[t._v("Add Movie")]),r("br"),r("br"),r("table",{staticClass:"table table-hover"},[t._m(0),r("tbody",t._l(t.movies,(function(e,o){return r("tr",{key:o},[r("td",[t._v(t._s(e.id))]),r("td",[t._v(t._s(e.name))]),r("td",[t._v(t._s(e.year))]),r("td",[t._v(t._s(e.genre))]),r("td",[t._v(t._s(e.director_id))]),r("td",[r("div",{staticClass:"btn-group",attrs:{role:"group"}},[r("button",{directives:[{name:"b-modal",rawName:"v-b-modal.movie-update-modal",modifiers:{"movie-update-modal":!0}}],staticClass:"btn btn-warning btn-sm",attrs:{type:"button"},on:{click:function(r){return t.editMovie(e)}}},[t._v(" Update ")]),r("button",{staticClass:"btn btn-danger btn-sm",attrs:{type:"button"},on:{click:function(r){return t.onDeleteMovie(e)}}},[t._v(" Delete ")])])])])})),0)])],1)]),r("b-modal",{ref:"addMovieModal",attrs:{id:"movie-modal",title:"Add a new movie","hide-footer":""}},[r("b-form",{staticClass:"w-100",on:{submit:t.onSubmit,reset:t.onReset}},[r("b-form-group",{attrs:{id:"form-name-group",label:"Name:","label-for":"form-name-input"}},[r("b-form-input",{attrs:{id:"form-name-input",type:"text",required:"",placeholder:"Enter name"},model:{value:t.addMovieForm.name,callback:function(e){t.$set(t.addMovieForm,"name",e)},expression:"addMovieForm.name"}})],1),r("b-form-group",{attrs:{id:"form-year-group",label:"Year:","label-for":"form-year-input"}},[r("b-form-input",{attrs:{id:"form-year-input",type:"text",required:"",placeholder:"Enter year"},model:{value:t.addMovieForm.year,callback:function(e){t.$set(t.addMovieForm,"year",e)},expression:"addMovieForm.year"}})],1),r("b-form-group",{attrs:{id:"form-genre-group",label:"Genre:","label-for":"form-genre-input"}},[r("b-form-select",{attrs:{options:t.options},model:{value:t.addMovieForm.genre,callback:function(e){t.$set(t.addMovieForm,"genre",e)},expression:"addMovieForm.genre"}})],1),r("b-form-group",{attrs:{id:"form-director-group",label:"Director ID:","label-for":"form-director-input"}},[r("b-form-input",{attrs:{id:"form-director-input",type:"text",required:"",placeholder:"Enter director ID"},model:{value:t.addMovieForm.director_id,callback:function(e){t.$set(t.addMovieForm,"director_id",e)},expression:"addMovieForm.director_id"}})],1),r("b-button-group",[r("b-button",{attrs:{type:"submit",variant:"primary"}},[t._v("Submit")]),r("b-button",{attrs:{type:"reset",variant:"danger"}},[t._v("Reset")])],1)],1)],1),r("b-modal",{ref:"editMovieModal",attrs:{id:"movie-update-modal",title:"Update","hide-footer":""}},[r("b-form",{staticClass:"w-100",on:{submit:t.onSubmitUpdate,reset:t.onResetUpdate}},[r("b-form-group",{attrs:{id:"form-name-edit-group",label:"ID:","label-for":"form-id-edit-input"}},[r("b-form-input",{attrs:{id:"form-id-edit-input",type:"text",required:"",placeholder:"Enter ID"},model:{value:t.editForm.id,callback:function(e){t.$set(t.editForm,"id",e)},expression:"editForm.id"}})],1),r("b-form-group",{attrs:{id:"form-name-edit-group",label:"Name:","label-for":"form-name-edit-input"}},[r("b-form-input",{attrs:{id:"form-name-edit-input",type:"text",required:"",placeholder:"Enter name"},model:{value:t.editForm.name,callback:function(e){t.$set(t.editForm,"name",e)},expression:"editForm.name"}})],1),r("b-form-group",{attrs:{id:"form-year-edit-group",label:"Year:","label-for":"form-year-edit-input"}},[r("b-form-input",{attrs:{id:"form-year-edit-input",type:"text",required:"",placeholder:"Enter year"},model:{value:t.editForm.year,callback:function(e){t.$set(t.editForm,"year",e)},expression:"editForm.year"}})],1),r("b-form-group",{attrs:{id:"form-genre-edit-group",label:"Genre:","label-for":"form-genre-edit-input"}},[r("b-form-select",{attrs:{options:t.options},model:{value:t.editForm.genre,callback:function(e){t.$set(t.editForm,"genre",e)},expression:"editForm.genre"}})],1),r("b-form-group",{attrs:{id:"form-director-edit-group",label:"Director ID:","label-for":"form-director-edit-input"}},[r("b-form-input",{attrs:{id:"form-director-edit-input",type:"text",required:"",placeholder:"Enter director"},model:{value:t.editForm.director_id,callback:function(e){t.$set(t.editForm,"director_id",e)},expression:"editForm.director_id"}})],1),r("b-button-group",[r("b-button",{attrs:{type:"submit",variant:"primary"}},[t._v("Update")]),r("b-button",{attrs:{type:"reset",variant:"danger"}},[t._v("Cancel")])],1)],1)],1)],1)},Y=[function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("thead",[r("tr",[r("th",{attrs:{scope:"col"}},[t._v("ID")]),r("th",{attrs:{scope:"col"}},[t._v("Name")]),r("th",{attrs:{scope:"col"}},[t._v("Year")]),r("th",{attrs:{scope:"col"}},[t._v("Genre")]),r("th",{attrs:{scope:"col"}},[t._v("Director ID")]),r("th")])])}],q={data:function(){return{options:[{value:null,text:"Please select a genre"},{value:"drama",text:"Drama"},{value:"action",text:"Action"},{value:"comedy",text:"Comedy"},{value:"horror",text:"Horror"}],movies:[],addMovieForm:{name:"",genre:null,year:"",director_id:""},message:"",showMessage:!1,editForm:{id:"",name:"",genre:null,year:"",director_id:""}}},components:{alert:M},methods:{getMovies:function(){var t=this,e="/api/movies";b.a.get(e).then((function(e){t.movies=e.data})).catch((function(t){console.error(t)}))},addMovie:function(t){var e=this,r="/api/movie";b.a.post(r,t).then((function(){e.getMovies(),e.message="movie added!",e.showMessage=!0})).catch((function(t){console.log(t),e.message=t,e.showMessage=!0,e.getMovies()}))},initForm:function(){this.addMovieForm.name="",this.addMovieForm.genre=null,this.addMovieForm.year="",this.addMovieForm.director_id="",this.editForm.id="",this.editForm.name="",this.editForm.genre=null,this.editForm.year="",this.editForm.director_id=""},onSubmit:function(t){t.preventDefault(),this.$refs.addMovieModal.hide();var e={name:this.addMovieForm.name,genre:this.addMovieForm.genre,year:this.addMovieForm.year,director_id:this.addMovieForm.director_id};this.addMovie(e),this.initForm()},onReset:function(t){t.preventDefault(),this.$refs.addMovieModal.hide(),this.initForm()},editMovie:function(t){this.editForm=t},onSubmitUpdate:function(t){t.preventDefault(),this.$refs.editMovieModal.hide();var e={id:this.editForm.id,name:this.editForm.name,genre:this.editForm.genre,year:this.editForm.year,director_id:this.editForm.director_id};this.updateMovie(e)},updateMovie:function(t){var e=this,r="/api/movie";b.a.put(r,t).then((function(){e.getMovies(),e.message="movie updated!",e.showMessage=!0})).catch((function(t){console.error(t),e.getMovies()}))},onResetUpdate:function(t){t.preventDefault(),this.$refs.editMovieModal.hide(),this.initForm(),this.getMovies()},removeMovie:function(t){var e=this,r="/api/movie";b.a.delete(r,{data:t}).then((function(){e.getMovies(),e.message="movie removed!",e.showMessage=!0})).catch((function(t){console.error(t),e.getMovies()}))},onDeleteMovie:function(t){var e={id:t.id};this.removeMovie(e)}},created:function(){this.getMovies()}},O=q,j=Object(d["a"])(O,S,Y,!1,null,null,null),N=j.exports,R=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",{staticClass:"container"},[r("button",{staticClass:"btn btn-primary",attrs:{type:"button"}},[t._v(t._s(t.msg))])])},I=[],P={name:"Ping",data:function(){return{msg:""}},methods:{getMessage:function(){var t=this,e="http://localhost:8000/ping";b.a.get(e).then((function(e){t.msg=e.data})).catch((function(t){console.error(t)}))}},created:function(){this.getMessage()}},G=P,T=Object(d["a"])(G,R,I,!1,null,null,null),J=T.exports;a["default"].use(l["a"]);var H=new l["a"]({mode:"history",base:"/",routes:[{path:"/actors",name:"Actors",component:w},{path:"/directors",name:"Directors",component:U},{path:"/movies",name:"Movies",component:N},{path:"/ping",name:"Ping",component:J}]});r("f9e3");a["default"].use(o["a"]),a["default"].config.productionTip=!1,new a["default"]({router:H,render:function(t){return t(m)}}).$mount("#app")},"85ec":function(t,e,r){}});
//# sourceMappingURL=app.3a5bf9c8.js.map