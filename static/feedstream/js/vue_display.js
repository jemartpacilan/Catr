Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
    el: '#starting',
    delimiters: ['${', '}'],
    data: {
        caterers: [],
        results: [],
        reviews: [],
        loading: true,
        message: null,
        searchTerm: '',
        catererMessage: '(hey!)',
        currentCaterer: {},
    },
    mounted: function() {
        this.getInitialData();
    },
    methods: {
        // fetch all caterers in database
        getInitialData: function() {
            // let api_url = '/api/caterers/';
            // this.loading = true;
            // this.$http.get(api_url)
            //     .then((response) => {
            //         this.caterers = response.data;
            //         this.results = response.data;
            //         this.loading = false;
            //         console.log(this.caterers)
            //     })
            //     .catch((err) => {
            //         this.loading = false;
            //     })

            let api_url = '/feedstream/ajax/reviewtotal/';
            this.loading = true;
            this.$http.get(api_url)
                .then((response) => {
                    // this.reviews = response.data.total;
                    this.results = this.caterers = response.data.caterers_data;
                    console.log(this.caterers);
                })
                .catch((err) => {
                    this.loading = false;
                })
        },
        // search on ener keypress
        enterSearch: function(e) {
            if (e.keyCode === 13) {
                this.searchResults();
            }
        },
        // search when button is clicked
        buttonSearch: function() {
          console.log('annyeong');
            this.searchResults();
        },
        // function that filters using starting characters of user input
        searchResults: function() {
            var val = this.searchTerm.toLowerCase();
            if (this.searchTerm !== '') {
                this.results = this.caterers.filter(function(item) {
                    // console.log(val)
                    return item.business_name.toLowerCase().startsWith(val.toLowerCase());
                });
                console.log(this.results.length);
                if (this.results.length === 0) {
                    this.results = this.caterers;
                }
            }
        },
        newCaterer: function(index) {
          // sorts caterers by average
          if(index == 0){
            this.caterers.sort(function(a, b){
              return b.average - a.average;
            });
          }
          // sorts caterers by date
          if(index == 4){
            this.caterers.sort(function(a, b) {
              var dateA = new Date(a.created_date);
              var dateB = new Date(b.created_date);
              return dateB - dateA;
            });
          }
        }
    },
    // added truncate function
    filters: {
        truncate: function(string, value) {
            if (string.length < value) return string;
            return string.substring(0, value) + '...';
        }
    },
    // input watcher for empty search, displays all items back
    watch: {
        'searchTerm': function(val, oldVal) {
            if (val === '') {
                this.results = this.caterers;
            }
        }
    }

});