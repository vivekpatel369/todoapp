<template>
  <main>
    <v-subheader class="title">Todos List
      <div>
        <v-btn primary fab small dark>
          <v-icon ripple color="white">add</v-icon>
        </v-btn>
      </div>
    </v-subheader>
    <v-spacer></v-spacer>
    <v-divider></v-divider>
    <v-container grid-list-md text-xs-center>
      <v-layout row wrap>
        <v-flex xs6 v-for="itemList in todolists">
          <v-list one-line headline>
            <v-subheader class="title">{{itemList.title}}</v-subheader>
            <v-layout row wrap>
              <v-flex sm8 style="padding: 0 16px;">
                <v-text-field
                  v-model="itemList['addNew']"
                  name="input-1-3"
                  label="Enter Something to add"
                  single-line
                ></v-text-field>
              </v-flex>
              <v-flex sm3>
                <v-btn @click="onAddbtnClick(itemList)" block primary>Add</v-btn>
              </v-flex>
            </v-layout>

            <v-list-tile v-for="item in itemList.todolist">
              <v-list-tile-action>
                <v-checkbox v-model="item.status" @change="onCheckboxChange(item)"></v-checkbox>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-dialog v-model="dialog" persistent>
                  <v-list-tile-title slot="activator"><span
                    v-bind:class="(item.status == false) ? '' : 'line'">{{item.title}}</span>
                  </v-list-tile-title>
                  <v-card>
                    <v-card-title>
                      <span class="headline">Edit Todos</span>
                    </v-card-title>
                    <v-card-text>
                      <v-text-field label="Enter Title to change" v-model="item['demo']"></v-text-field>
                    </v-card-text>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn color="blue darken-1" flat @click.native="dialog = false">Close
                      </v-btn>
                      <v-btn color="blue darken-1" flat @click.native="dialog = false"
                             @click="onTitleChange(item)">Save
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
              </v-list-tile-content>
              <v-list-tile-action>
                <v-btn icon ripple @click="onDeleteBtn(itemList,item)">
                  <v-icon color="grey lighten-1">delete</v-icon>
                </v-btn>
              </v-list-tile-action>
            </v-list-tile>
          </v-list>
          <v-layout row wrap style="justify-content: center;">
            <v-flex sm4>
              <v-btn block primary outline @click="filter('all')">All</v-btn>
            </v-flex>
            <v-flex sm4>
              <v-btn block primary outline @click="filter('completed')">Completed</v-btn>
            </v-flex>
            <v-flex sm4>
              <v-btn block primary outline @click="filter('pendding')">Pendding</v-btn>
            </v-flex>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-container>
  </main>
</template>
<script>
  import todos_api from '@/services/todos'

  export default {
    methods: {
      onAddbtnClick(itemList) {
        if (itemList.addNew != "") {
          todos_api.addItem({'title': itemList.addNew, 'list': itemList.id}).then(res => {
            this.todolists[itemList.id -1].todolist.push(res.data)
            itemList.addNew = ''
          }).catch(error => {
            console.log("VIVEK", error);
          })
        }
      },
      onDeleteBtn(itemList,item) {
        todos_api.deleteItem({'id': item.id}).then(res => {
          this.todolists[itemList.id -1].todolist.pop(item)
        }).catch(error => {
          console.log("VIVEK", error);
        })
      },
      onCheckboxChange(item) {
        //item.status = (item.status) ? false : true
        console.log(item.id);
        todos_api.updateItem(item).then(res => {
        }).catch(error => {
          console.log("VIVEK", error);
        })
      },
      onTitleChange(item) {
        item.addNew = item.addNew
        //console.log(item.title);
        todos_api.updateItem(item).then(res =>{
          console.log("Hello");
        }).catch(error => {
          console.log("VIVEK", error);
        })
      },
      filter(type) {
        switch (type) {
          case 'completed':
            this.filterData = this.responseData.filter(function (data) {
              if (data.status == true) {
                //console.log("DATA", data);
                return data
              }
            })
            break;
          case 'pendding':
            this.filterData = this.responseData.filter(function (data) {
              if (data.status == false) {
                //console.log("DATA", data);
                return data
              }
            })
            break;
          default:
            this.filterData = this.responseData
        }
      }
    },
    mounted() {
      todos_api.getTodoList().then(response => {
        this.todolists = response.data
//        console.log("DEMO DATA",this.todolist);
//        for (var key in this.todolist) {
//          console.log("DEMO DATA",this.todolist[key].todolist);
//        }
//        this.responseData = this.todolist.todolist
//        this.filterData = this.todolist.todolist
//        console.log("DEMO",this.todolist)
      })
    },
    data() {
      return {
        notifications: false,
        sound: true,
        widgets: false,
        responseData: [],
        list: null,
        addinput: '',
        addTitle: '',
        dialog: false,
        todolists: null
      }
    }
  }
</script>

<style lang="scss">
  .line {
    text-decoration: line-through;
  }

  .list__tile__content {
    padding-left: 30px;
  }
</style>
