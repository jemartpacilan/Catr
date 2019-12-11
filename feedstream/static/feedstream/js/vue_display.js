Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
    el: '#starting',
    delimiters: ['${', '}'],
    data: {
        caterers: [],
        results: [],
        reviews: [],
        buffer: true,
        nearmeIsClicked: false,
        currentLocation: {
            'coords' : {
                'latitude' : 10.343017,
                'longitude' : 123.920782
            }
        },
        loading: true,
        message: null,
        searchTerm: '',
        catererMessage: '(hey!)',
        currentCaterer: {},
    },
    created: function() {

    },
    mounted: function() {
        this.initLocation();
        this.nearmeIsClicked = false;
        this.getInitialData();
    },
    methods: {
        initLocation: function() {
            // var currentLocation;
            var vm = this;
            if ("geolocation" in navigator) {
                navigator.geolocation.getCurrentPosition((position) => {
                    this.currentLocation = position;
                });
            } else {
                alert('geolocation is not available in your browser');
            }

            console.log("Triggered geolocation...");
        },
        // fetch all caterers in database
        getInitialData: function() {
            let api_url = '/feedstream/ajax/reviewtotal/';
            this.loading = true;
            this.$http.get(api_url)
                .then((response) => {
                    this.results = this.caterers = response.data.caterers_data;
                    this.getLocations();
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
            this.searchResults();
        },
        // function that filters using starting characters of user input
        searchResults: function() {
            var val = this.searchTerm.toLowerCase();
            if (this.searchTerm !== '') {
                this.results = this.caterers.filter(function(item) {
                    return item.caterer.business_name.toLowerCase().startsWith(val.toLowerCase());
                });
                if (this.results.length === 0) {
                    this.results = this.caterers;
                }
            }
        },
        calculateDistance: function(coordinates){
            var R = 6371e3; // metres
            var lat1 = this.currentLocation.coords.latitude
            var lat2 = coordinates.Latitude
            var lon1 = this.currentLocation.coords.longitude
            var lon2 = coordinates.Longitude
            // var R = 6371e3; // Radius of the earth in km
            var dLat = (lat2 - lat1) * Math.PI / 180;  // deg2rad below
            var dLon = (lon2 - lon1) * Math.PI / 180;
            var a = 0.5 - Math.cos(dLat)/2 +
                Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *
                (1 - Math.cos(dLon))/2;

            return R * 2 * Math.asin(Math.sqrt(a));
        },
        newCaterer: function(index) {
          // sorts caterers by average
          if(index == 0){
            this.nearmeIsClicked = false;
            this.caterers.sort(function(a, b){
              return b.average - a.average;
            });
          }
          if(index == 1){
            this.nearmeIsClicked = true;
            if(!this.buffer){
                this.caterers.sort(function(a, b) {
                  return a.distance - b.distance;
                });
            }
            // this.getLocations();
          }
          // sorts caterers by date
          if(index == 4){
            this.nearmeIsClicked = false;
            this.caterers.sort(function(a, b) {
              var dateA = new Date(a.caterer.created_date);
              var dateB = new Date(b.caterer.created_date);
              return dateB - dateA;
            });
          }
        },
        async getLocations(){
            for(let i = 0; i < this.caterers.length; ++i){
                address = this.caterers[i].caterer.street_address +
                    ' ' + this.caterers[i].caterer.municipality_address;
                address = address.split(/[\s,]+/).join('+');
                // console.log(address)
                var vm = this;
                await new Promise(next => {
                    this.getLocationViaHERE(address).then(function(data) {
                        coordinates = data;
                        vm.caterers[i].distance = vm.calculateDistance(coordinates);
                        next();
                    });
                })
            }
            this.buffer = false;
            $('.stars').stars();
        },
        getLocationViaHERE: function(location) {
            var unres_coords = new Promise(function(resolve, reject) {
                $.ajax({
                    url: 'https://geocoder.cit.api.here.com/6.2/geocode.json?app_id=jlSvwwwjsXosoDszZSTF&app_code=pAvc11w29ynkyotNn4vQ6A&searchtext=' + location
                }).then(function(data) {
                    resolve(data.Response.View[0].Result[0].Location.DisplayPosition);
                });
            });
            return unres_coords;
        }
    },
    // added truncate function
    filters: {
        truncate: function(string, value) {
            if (string.length < value) return string;
            return string.substring(0, value) + '...';
        },
        truncateNum: function(string, value) {
            if (string.length < value) return string;
            return string.toString().substring(0, value);
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