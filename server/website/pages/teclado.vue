<template>
  <section class="container section">
    <div>
      <b-button class="button is-link" @click="onTeclear('1')">1</b-button>
      <b-button class="button is-link" @click="onTeclear('2')">2</b-button>
      <b-button class="button is-link" @click="onTeclear('3')">3</b-button>
    </div>
    <div>
      <b-button class="button is-link" @click="onTeclear('4')">4</b-button>
      <b-button class="button is-link" @click="onTeclear('5')">5</b-button>
      <b-button class="button is-link" @click="onTeclear('6')">6</b-button>
    </div>
    <div>
      <b-button class="button is-link" @click="onTeclear('7')">7</b-button>
      <b-button class="button is-link" @click="onTeclear('8')">8</b-button>
      <b-button class="button is-link" @click="onTeclear('9')">9</b-button>
    </div>
    <div>
      <b-button class="button is-link" @click="onTeclear('L')">*</b-button>
      <b-button class="button is-link" @click="onTeclear('L')">0</b-button>
      <b-button class="button is-link" @click="onTeclear('L')">#</b-button>
    </div>
    <div>
      <p>{{ pantalla }}</p>
    </div>
  </section>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  layout: 'blank',
  computed: {
    ...mapState({
      pantalla: (state) => state.iglesia.pantalla
    })
  },
  mounted() {
    this.conseguirPantalla()
  },
  methods: {
    ...mapActions({
      editarPantalla: 'iglesia/editarPantalla',
      conseguirPantalla: 'iglesia/conseguirPantalla'
    }),
    async onTeclear(indexEvento) {
      await this.editarPantalla({ index_evento: indexEvento })
      await this.conseguirPantalla()
    }
  }
}
</script>

<style scoped>
img {
  height: 60px;
}
.margen_abajo {
  margin-bottom: 25px;
}
</style>
