<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
        <div class="hero-body has-text-centered">
            <p class="title mb-6">
                Welcome to Djacket
            </p>
            <p class="subtitle">
                The best jacket store online
            </p>
        </div>
    </section>

    <div class="columns is-multiline">
        <div class="column is-12">
            <h2 class="is-size-2 has text-centered">Categories</h2>
        </div>


        <div
            class="column is-3"
            v-for="category in shopCategories"
            bind:key="category.id"
        >

        <h3 class="is-size-4">{{ category.title}}</h3>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Home',
    data() {
        return{
            shopCategories: []
        }
    },
    components: {
    },
    mounted(){
        this.getShopCategories()
    },
    methods: {
       getShopCategories(){
            axios
                .get('/api/products/categories/')
                .then(response => {
                    this.shopCategories = response.data
                })
                .catch(error => {
                  console.log(error)
                })
       }
    }
}
</script>