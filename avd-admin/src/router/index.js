import Vue from 'vue'
import Router from 'vue-router'
import TodosList from '@/components/todos/TodosList'
import Login from '@/components/signin/Login'

Vue.use(Router)


let router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/login',
      name: 'Login',
      components: {
        default: Login,
      }
    }, 
    {
      path: '/',
      name: 'Todos',
      components: {
        default: TodosList,
      },
      meta: {
        isProtected: true
      }
      // beforeEnter: (to, from, next) => {
      //   if(window.localStorage.getItem('token') == ""){
      //     router.push('/login');
      //   }
      // }
    }

  ],

})

router.beforeEach(function (to, from, next) {
  var token = window.localStorage.getItem('token')
  if (to.matched.some(record => record.meta.isProtected) && !token ){
      console.log("demo in token")
      next('/login')  
  }else{
    window.scrollTo(0, 0)
    next()
}
  
  
})

export default router
