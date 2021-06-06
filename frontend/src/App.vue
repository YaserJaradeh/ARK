<template>
  <div id="app">
    <v-shell
      :banner="banner"
      :shell_input="send_to_terminal"
      :commands="commands"
      @shell_output="prompt"
    ></v-shell>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      send_to_terminal: "",
      banner: {
        header: "ARK (Using NLP to make gaming more fun)",
        subHeader: "Enjoy your journey with us. Currently loaded story: <<PhD Life>>",
        helpHeader: 'Enter "help" for more information.',
        emoji: {
          first: "🤖",
          second: "📝",
          time: 750
        },
        sign: `ARK #`,
        img: {
          align: "left",
          link: "https://i.ibb.co/pXXJNVG/Untitled-1.png",
          width: 100,
          height: 100
        }
      },
      commands: [
        {
          name: "info",
          get() {
            return `Quick note: just follow the story and write what you think should be done!`;
          }
        },
        {
          name: "restart",
          get() {
            return `Restarting the <span style="color:red"><b>ARK</b></span> for you`;
          }
        }
      ]
    };
  },
  methods: {
    prompt(value) {
      if (value.trim() === "ifconfig") {
        this.send_to_terminal = `
    Wi-Fi wireless network card:
        
    Local link IPv6 address. . . : fe80 :: 340f: 6f02: 41e9: 477b% 24
    IPv4 address. . . . . . . . .: 192.168.1.2
    Subnet mask. . . . . . . . . : 255.255.255.0
    Default Gateway. . . . . . . : 192.168.1.1`;
      } else {
        this.send_to_terminal = `'${value}' is not recognized as an internal command or external,
an executable program or a batch file`;
      }
    }
  }
};
</script>

<style>
</style>
