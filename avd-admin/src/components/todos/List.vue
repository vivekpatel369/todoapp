<template>
    <main>
      <v-container xs8 offset-xs2>
        <v-list one-line headline>
          <v-subheader class="title">Todos List</v-subheader>
            <v-layout wrap>
                <v-flex sm10 style="padding: 0 16px;">
                    <v-text-field
                        v-model="addinput"
                        name="input-1-3"
                        label="Enter Something to add"
                        single-line
                    ></v-text-field>
                </v-flex>
                <v-flex sm2>
                    <v-btn @click="onAddbtnClick" block primary>Add</v-btn>
                </v-flex>
            </v-layout>

          <v-list-tile v-for="item in filterData">
            <v-list-tile-action>
              <v-checkbox v-model="item.status" @change="onCheckboxChange(item)"></v-checkbox>
            </v-list-tile-action>
            <v-list-tile-content>
                <v-dialog v-model="dialog" persistent>
                <v-list-tile-title slot="activator"><span v-bind:class="(item.status == false) ? '' : 'line'">{{item.title}}</span></v-list-tile-title>       
                <v-card>
                    <v-card-title>
                    <span class="headline">Edit Todos</span>
                    </v-card-title>
                    <v-card-text>
                        <v-text-field label="Enter Title to change" v-model="addTitle" ></v-text-field>
                    </v-card-text>
                    <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue darken-1" flat @click.native="dialog = false">Close</v-btn>
                    <v-btn color="blue darken-1" flat @click.native="dialog = false" @click="onTitleChange(item)">Save</v-btn>
                    </v-card-actions>
                </v-card>
                </v-dialog>
            </v-list-tile-content>
            <v-list-tile-action>
              <v-btn icon ripple @click="onDeleteBtn(item)" >
                <v-icon color="grey lighten-1">delete</v-icon>
              </v-btn>
            </v-list-tile-action>
          </v-list-tile>
        </v-list>
        
        <v-layout wrap style="justify-content: center;">
            <v-flex sm2>
                <v-btn block primary outline @click="filter('all')">All</v-btn>
            </v-flex>
            <v-flex sm2>
                <v-btn block primary outline @click="filter('completed')">Completed</v-btn>
            </v-flex>
            <v-flex sm2>
                <v-btn block primary outline @click="filter('pendding')">Pendding</v-btn>
            </v-flex>
        </v-layout>
        
      </v-container>
    </main>
</template>
<script>
    import todos_api from '@/services/todos'
    export default {
        methods :{
            onAddbtnClick(){
                if(this.addinput != ""){
                    todos_api.addItem({'title': this.addinput}).then(res=>{
                        this.responseData.push(res.data)
                        console.log(this.responseData)
                        this.addinput = ''
                    }).catch(error=>{
                        console.log("VIVEK", error);
                    })
                }
            },
            onDeleteBtn(item){
                todos_api.deleteItem({'id': item.id}).then(res=>{
                    this.responseData.pop(item)
                }).catch(error=>{
                    console.log("VIVEK", error);
                })
            },
            onCheckboxChange(item){
                //item.status = (item.status) ? false : true
                console.log(item.id);
                todos_api.updateItem(item).then(res=>{    
                }).catch(error=>{
                    console.log("VIVEK", error);
                })
            },
            onTitleChange(item){
                item.title = this.addTitle
                console.log(item.title);
                todos_api.updateItem(item).then(res=>{    
                }).catch(error=>{
                    console.log("VIVEK", error);
                })
            },
            filter(type){
                switch(type) {
                    case 'completed':
                        this.filterData = this.responseData.filter(function (data) {
                            if(data.status == true){
                                console.log("DATA", data);
                                return data
                            }
                        })
                        break;
                    case 'pendding':
                        this.filterData = this.responseData.filter(function (data) {
                            if(data.status == false){
                                console.log("DATA", data);
                                return data
                            }
                        })
                        break;
                    default:
                        this.filterData =  this.responseData
                }
            }
        },
        mounted (){
            todos_api.getList().then(response => {
                this.responseData = response.data
                this.filterData = response.data
                console.log(this.responseData)
            })
        },
        data () {
            return {
                notifications: false,
                sound: true,
                widgets: false,
                responseData: null,
                filterData: null,
                addinput: '',
                addTitle: '',
                dialog: false,
                numbers: [ 1, 2, 3, 4, 5 ]
            }
        }
  }
</script>

<style lang="scss">
    .line {
		text-decoration: line-through;
	}
    .list__tile__content{
        padding-left: 30px;
    }
</style>
