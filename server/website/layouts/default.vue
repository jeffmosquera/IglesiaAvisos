<template>
  <div>
    <section class="hero is-success">
      <div class="hero-body">
        <div class="container has-text-centered">
          <div><img src="~/assets/logo.png" /></div>
          <b-button
            class="button is-link"
            size="is-medium"
            @click="onCerrarSesion"
            >Cerrar</b-button
          >
        </div>
      </div>

      <div class="hero-foot">
        <nav class="tabs is-boxed is-fullwidth is-large">
          <div class="container">
            <b-tabs v-model="activeTab" type="is-boxed">
              <b-tab-item
                label="EVENTOS"
                icon="google-photos"
                size="is-large"
              ></b-tab-item>
              <b-tab-item
                label="USUARIOS"
                icon="account"
                size="is-large"
              ></b-tab-item>
            </b-tabs>
          </div>
        </nav>
      </div>
    </section>

    <div class="container section">
      <nuxt />
    </div>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'
export default {
  data() {
    return {
      activeTab: 0
    }
  },
  watch: {
    activeTab(val) {
      if (val === 0) {
        this.$router.push('/eventos')
      } else if (val === 1) {
        this.$router.push('/usuarios')
      }
    }
  },
  methods: {
    ...mapMutations({
      cerrarSesion: 'iglesia/cerrarSesion'
    }),
    onCerrarSesion() {
      this.cerrarSesion()
      this.$router.push('/')
    }
  }
}
</script>

<style>
.columns {
  margin-left: +0.75rem;
  margin-right: +0.75rem;
}
.marcas {
  background-color: #fafafa;
}
.principal {
  padding-top: 40px;
  padding-bottom: 40px;
}
.footer1 {
  background-color: #000000;
}
.navbar-burger {
  color: #ffffff;
}
.navbar-brand a:hover {
  color: #ffffff;
}
.fix-footer {
  position: absolute;
  width: 100%;
  bottom: 0;
  overflow: hidden;
}
</style>
